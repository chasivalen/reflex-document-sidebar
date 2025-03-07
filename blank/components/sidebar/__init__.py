# Sample data
data = {
    "versions": ["1.0.1", "1.1.0-alpha", "2.0.0-beta1"],
    "nav_main": [
        {
            "title": "Getting Started",
            "url": "#",
            "items": [
                {
                    "title": "Installation",
                    "url": "#",
                    "is_active": False,
                },
                {
                    "title": "Project Structure",
                    "url": "#",
                    "is_active": False,
                },
            ],
        },
        {
            "title": "Building Your Application",
            "url": "#",
            "items": [
                {
                    "title": "Routing",
                    "url": "#",
                    "is_active": False,
                },
                {
                    "title": "Data Fetching",
                    "url": "#",
                    "is_active": True,
                },
                {
                    "title": "Rendering",
                    "url": "#",
                    "is_active": False,
                },
                # Additional items omitted for brevity
            ],
        },
        {
            "title": "API Reference",
            "url": "#",
            "items": [
                {
                    "title": "Components",
                    "url": "#",
                    "is_active": False,
                },
                {
                    "title": "File Conventions",
                    "url": "#",
                    "is_active": False,
                },
                # Additional items omitted for brevity
            ],
        },
        {
            "title": "Architecture",
            "url": "#",
            "items": [
                {
                    "title": "Accessibility",
                    "url": "#",
                    "is_active": False,
                },
                {
                    "title": "Fast Refresh",
                    "url": "#",
                    "is_active": False,
                },
                # Additional items omitted for brevity
            ],
        },
    ],
}

from .dashboard_page import dashboard_page
from .sidebar import sidebar
__all__ =["sidebar", "dashboard_page"]