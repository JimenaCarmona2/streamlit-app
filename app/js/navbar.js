(function() {{
    const dropdown = document.getElementById('mainDropdown');
    const btn = document.getElementById('dropBtn');
    
    btn.addEventListener('click', function(e) {{
        e.stopPropagation();
        const isOpen = dropdown.classList.contains('open');
        dropdown.classList.toggle('open', !isOpen);
        btn.setAttribute('aria-expanded', String(!isOpen));
    }});

    dropdown.addEventListener('mouseenter', () => {{
        dropdown.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
    }});
    
    dropdown.addEventListener('mouseleave', () => {{
        if (!dropdown.matches(':focus-within')) {{
            dropdown.classList.remove('open');
            btn.setAttribute('aria-expanded', 'false');
        }}
    }});

    document.addEventListener('click', function(e) {{
        if (!dropdown.contains(e.target)) {{
            dropdown.classList.remove('open');
            btn.setAttribute('aria-expanded', 'false');
        }}
    }});

    dropdown.querySelectorAll('a').forEach(a => {{
        a.addEventListener('click', () => {{
            dropdown.classList.remove('open');
            btn.setAttribute('aria-expanded', 'false');
        }});
    }});
}})();