function serveMenu(site_detail) {
    document.querySelector('#menu-btn').onclick = function() {
        createMenu(site_detail.site_name.url, site_detail.site_name.tc);
        createMenu(site_detail.site_home.url, site_detail.site_home.tc);
        createMenu(site_detail.products.url, site_detail.products.tc);
        let rmMenu = document.createElement('button');
        rmMenu.setAttribute('id','rm-menu-btn');
        rmMenu.textContent = 'Close Menu';
        const menuContainer = document.querySelector('#menu-container');
        menuContainer.appendChild(rmMenu);
        removeMenu();
    }
}

function createMenu(url, tc) {
    let menuContainer = document.querySelector('#menu-container');
    let menuItem = document.createElement('a');
    menuItem.setAttribute('href',url);
    menuItem.setAttribute('class','menu-item');
    menuItem.textContent = tc;
    menuContainer.appendChild(menuItem);
}

function removeMenu() {
    const menuContainer = document.querySelector('#menu-container');
    document.querySelector('#rm-menu-btn').onclick = function() {
        while (menuContainer.firstChild) {
            menuContainer.removeChild(menuContainer.lastChild);
        }
    }
}
export {serveMenu}
