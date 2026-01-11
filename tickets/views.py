from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from .models import Ticket
from .forms import TicketForm
from .services.automation import auto_assign_category, auto_assign_priority
from django.shortcuts import render, get_object_or_404, redirect
# --- 1. THE TRAFFIC CONTROLLER ---
@login_required
def login_redirect(request):
    """
    Checks the user's role immediately after login and 
    redirects them to the appropriate dashboard.
    """
    if request.user.is_superuser:
        return redirect('/admin/')
    elif request.user.is_staff  :
        return redirect('technician_dashboard')
    
    else:
        return redirect('dashboard')

# --- 2. USER VIEWS ---
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.category = auto_assign_category(ticket.description)
            ticket.priority = auto_assign_priority(ticket.description)
            ticket.save()

            messages.success(request, f'Ticket #{ticket.id} created successfully!')
            return redirect('my_tickets')
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tickets/my_tickets.html', {'tickets': tickets})


@login_required
def dashboard(request):
    # Fetch tickets only for the logged-in user
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tickets/dashboard.html', {'tickets': tickets}) # Add the 'tickets/' prefix

# --- 3. TECHNICIAN VIEWS ---
@login_required
def technician_dashboard(request):
    # 1. Security Check
    if not request.user.is_staff:
        messages.error(request, "Access denied. Only technicians can view this page.")
        return redirect('dashboard')

    # 2. Filter tickets ONLY assigned to the current technician
    # We use .filter(assigned_to=request.user) instead of .all()
    user_tickets = Ticket.objects.filter(assigned_to=request.user).order_by('-created_at')

    # 3. Calculate statistics based on the technician's specific tickets
    context = {
        'tickets': user_tickets,
        'unassigned_count': Ticket.objects.filter(assigned_to__isnull=True).count(), # Global pool
        'in_progress_count': user_tickets.filter(status='in_progress').count(),
        'urgent_count': user_tickets.filter(priority='high').exclude(status='closed').count(),
    }
    
    return render(request, 'tickets/technician_dashboard.html', context)
@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    
    # If the technician updates the status
    if request.method == 'POST':
        new_status = request.POST.get('status')
        ticket.status = new_status
        ticket.save()
        return redirect('technician_dashboard')
        
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})