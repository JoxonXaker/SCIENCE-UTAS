from django.utils.translation import gettext_lazy as _

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "",
    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Science-Utas Admin Panel",
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "web/logo/main_logo.svg",
    # Relative path to logo for your site, used for login logo (must be present in static files. Defaults to site_logo)
    "login_logo": "web/logo/main_logo.svg",
    # Logo to use for login form in dark themes (must be present in static files. Defaults to login_logo)
    # "login_logo_dark": "logo/logo_dark.svg",
    # CSS classes that are applied to the logo
    "site_logo_classes": "",
    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "logo/favicon.svg",
    # Welcome text on the login screen
    "welcome_sign": "Welcome Science-Utas Control Panel!",
    # Copyright on the footer
    "copyright": "Jahongir Turaqulov",
    # List of model admins to search from the search bar, search bar omitted if excluded
    # If you want to use a single search field you dont need to use a list, you can use a simple string
    "search_model": ["account.customuser", "article.articlemodel"],
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar":  "ImageField/URLField/Charfield",
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": _("Home"), "url": "home", "permissions": ["auth.view_user"]},
        {"name": _("About"), "url": "home", "permissions": ["auth.view_user"]},
        {"name": _("Contact"), "url": "contact", "permissions": ["auth.view_user"]},


        # external url that opens in a new window (Permissions can be added)
        # {"name": _("Support"), "url": "https://github.com/joxonxaker", "new_window": True},
        # model admin to link to (Permissions checked against model)
        # {"account": "account"},
        # {"app": "app"},
        # {"dinamic": "dinamic"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [
        # {"model": "account.customuser", "permissions": ["auth.view_user"]},
        {"name": "Support", "url": "https://github.com/joxonxaker", "new_window": True, "icon": "fas fa-comments"},
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps to base side menu (app or model) ordering off of
    "order_with_respect_to": ["Make Messages", "account", "articlemodel"],
    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "loans": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["loans.view_loan"],
            },
            # {"name": "Custom View", "url": "admin:custom_view", "icon": "fas fa-box-open"},
        ]
    },
    # Custom icons for side menu apps/models See the link below
    # https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,
    # 5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "account.CustomUser": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
        "journal.journalmodel": "fas fa-journal-whills",
        "journal.organizationmodel": "fas fa-university",
        "article.articlemodel": "fas fa-folder-open",
        "article.commentmodel": "fas fa-envelope",
        "article.deadlinemodel": "fas fa-hourglass",
        "dinamic.aboutmodel": "fas fa-photo-video",
        # "dinamic.aboutmodel": "fas fa-book",
        # "dinamic.aboutmodel": "fas fa-book-open",
        # "dinamic.aboutmodel": "fas fa-book-reader",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #################
    # Related Modal #
    #################
    # Activate Bootstrap modal
    "related_modal_active": False,
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cerulean",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
}