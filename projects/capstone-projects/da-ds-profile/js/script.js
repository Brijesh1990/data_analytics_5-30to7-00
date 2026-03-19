document.addEventListener('DOMContentLoaded', () => {

    // -----------------------------------------
    // Left Sidebar Drawer Logic
    // -----------------------------------------
    const hamburgerBtn = document.getElementById('mobile-menu-button');
    const sidebar      = document.getElementById('mobile-sidebar');
    const overlay      = document.getElementById('sidebar-overlay');
    const closeBtn     = document.getElementById('sidebar-close-btn');
    const mobileLinks  = document.querySelectorAll('.mobile-link');

    function openSidebar() {
        sidebar.classList.remove('-translate-x-full');
        overlay.classList.remove('opacity-0', 'pointer-events-none');
        overlay.classList.add('opacity-100');
        hamburgerBtn.classList.add('is-open');     // triggers CSS animation → X
        document.body.classList.add('overflow-hidden'); // prevent background scroll
    }

    function closeSidebar() {
        sidebar.classList.add('-translate-x-full');
        overlay.classList.remove('opacity-100');
        overlay.classList.add('opacity-0', 'pointer-events-none');
        hamburgerBtn.classList.remove('is-open');  // revert CSS animation → ☰
        document.body.classList.remove('overflow-hidden');
    }

    // Open on hamburger click
    hamburgerBtn.addEventListener('click', openSidebar);

    // Close on X button inside sidebar
    closeBtn.addEventListener('click', closeSidebar);

    // Close on overlay click
    overlay.addEventListener('click', closeSidebar);

    // Close automatically when any nav link is clicked
    mobileLinks.forEach(link => {
        link.addEventListener('click', closeSidebar);
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeSidebar();
    });

    // -----------------------------------------
    // Navbar Scroll Effect (Sticky Styling)
    // -----------------------------------------
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 20) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });
});
