// Component Loader for Ojingeo Hotel Website
function loadFooter() {
    fetch('components/footer.html')
        .then(response => response.text())
        .then(data => {
            // Insert footer before closing body tag
            document.body.insertAdjacentHTML('beforeend', data);
        })
        .catch(error => {
            console.error('Error loading footer component:', error);
            // Fallback: add footer directly if component fails to load
            const footerHTML = '<div class="demo-footer">Visual Demonstration: Focused on UI/UX. No data is stored or processed.</div>';
            document.body.insertAdjacentHTML('beforeend', footerHTML);
        });
}

// Load footer when DOM is fully loaded
document.addEventListener('DOMContentLoaded', loadFooter);
