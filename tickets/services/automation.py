"""
Automation service for IT Ticket System.
Provides keyword-based automatic assignment of ticket categories and priorities.
"""


def auto_assign_category(description: str) -> str:
    """
    Automatically assign a ticket category based on keywords in the description.
    
    Args:
        description (str): The ticket description text
        
    Returns:
        str: Category code ('hardware', 'software', 'network', 'access', or 'other')
    """
    # Convert description to lowercase for case-insensitive matching
    desc_lower = description.lower()
    
    # Hardware-related keywords
    hardware_keywords = [
        'mouse', 'keyboard', 'monitor', 'screen', 'laptop', 'desktop',
        'printer', 'scanner', 'hardware', 'device', 'computer', 'pc',
        'cable', 'headset', 'webcam', 'charger', 'battery', 'power',
        'broken', 'damaged', 'physical'
    ]
    
    # Software-related keywords
    software_keywords = [
        'software', 'application', 'app', 'program', 'install', 'uninstall',
        'update', 'upgrade', 'crash', 'error', 'bug', 'freeze', 'slow',
        'license', 'office', 'outlook', 'excel', 'word', 'browser',
        'chrome', 'firefox', 'windows', 'macos', 'operating system'
    ]
    
    # Network-related keywords
    network_keywords = [
        'network', 'internet', 'wifi', 'wi-fi', 'connection', 'disconnect',
        'vpn', 'ethernet', 'router', 'modem', 'bandwidth', 'speed',
        'online', 'offline', 'connectivity', 'ping', 'dns', 'ip',
        'server', 'email', 'cannot connect', 'no internet'
    ]
    
    # Access-related keywords
    access_keywords = [
        'access', 'permission', 'login', 'password', 'reset password',
        'account', 'locked', 'locked out', 'cannot login', 'credentials',
        'authentication', 'authorized', 'unauthorized', 'user', 'rights',
        'forgot password', 'expire', 'token', 'mfa', '2fa'
    ]
    
    # Count keyword matches for each category
    hardware_score = sum(1 for keyword in hardware_keywords if keyword in desc_lower)
    software_score = sum(1 for keyword in software_keywords if keyword in desc_lower)
    network_score = sum(1 for keyword in network_keywords if keyword in desc_lower)
    access_score = sum(1 for keyword in access_keywords if keyword in desc_lower)
    
    # Determine category based on highest score
    scores = {
        'hardware': hardware_score,
        'software': software_score,
        'network': network_score,
        'access': access_score
    }
    
    # Get category with highest score
    max_score = max(scores.values())
    
    # If no keywords matched, return 'other'
    if max_score == 0:
        return 'other'
    
    # Return category with highest score
    for category, score in scores.items():
        if score == max_score:
            return category
    
    return 'other'


def auto_assign_priority(description: str) -> str:
    """
    Automatically assign a ticket priority based on keywords in the description.
    
    Args:
        description (str): The ticket description text
        
    Returns:
        str: Priority level ('low', 'medium', 'high', or 'critical')
    """
    # Convert description to lowercase for case-insensitive matching
    desc_lower = description.lower()
    
    # Critical priority keywords - urgent issues affecting many users or critical systems
    critical_keywords = [
        'critical', 'urgent', 'emergency', 'down', 'outage', 'system down',
        'server down', 'network down', 'cannot work', 'production', 
        'all users', 'entire', 'complete failure', 'data loss', 'security breach',
        'hacked', 'virus', 'malware', 'ransomware', 'asap', 'immediately'
    ]
    
    # High priority keywords - significant impact on work
    high_keywords = [
        'high', 'important', 'blocking', 'cannot access', 'not working',
        'broken', 'failed', 'error', 'crash', 'multiple users',
        'business critical', 'deadline', 'today', 'stopped working'
    ]
    
    # Low priority keywords - minor issues or requests
    low_keywords = [
        'low', 'minor', 'question', 'request', 'how to', 'enhancement',
        'feature', 'cosmetic', 'sometime', 'whenever', 'not urgent',
        'nice to have', 'suggestion', 'inquiry'
    ]
    
    # Check for critical keywords first
    for keyword in critical_keywords:
        if keyword in desc_lower:
            return 'critical'
    
    # Check for high priority keywords
    for keyword in high_keywords:
        if keyword in desc_lower:
            return 'high'
    
    # Check for low priority keywords
    for keyword in low_keywords:
        if keyword in desc_lower:
            return 'low'
    
    # Default to medium priority if no specific keywords found
    return 'medium'