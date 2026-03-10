document.addEventListener('DOMContentLoaded', () => {
    // -----------------------------------------
    // Mobile Menu Toggle Logic
    // -----------------------------------------
    const btn = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');
    const icon = document.getElementById('menu-icon');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    btn.addEventListener('click', () => {
        // Toggle the visibility of the mobile menu
        menu.classList.toggle('hidden');
        
        // Toggle Icon between Hamburger and Close (X) mark
        if (menu.classList.contains('hidden')) {
            // Hamburger icon
            icon.setAttribute('d', 'M4 6h16M4 12h16M4 18h16'); 
        } else {
            // Close icon
            icon.setAttribute('d', 'M6 18L18 6M6 6l12 12'); 
        }
    });

    // Close Mobile Menu automatically when a link is clicked
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            menu.classList.add('hidden');
            icon.setAttribute('d', 'M4 6h16M4 12h16M4 18h16');
        });
    });

    // -----------------------------------------
    // Navbar Scroll Effect (Sticky Styling)
    // -----------------------------------------
    const navbar = document.getElementById('navbar');
    
    // Add a shadow and change opacity slightly when the user scrolls down
    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
});
