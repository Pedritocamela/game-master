const api_url = '/api/games';
let games = [];
let current_platform = 'all';

async function load_games() {
    try {
        const response = await fetch(api_url);
        games = await response.json();
        render_games();
        update_hero();
    } catch (error) {
        console.error('Error cargando juegos:', error);
    }
}

function render_games() {
    const grid = document.getElementById('games-grid');
    const filtered = current_platform === 'all' 
        ? games 
        : games.filter(g => g.platform.toLowerCase().includes(current_platform.toLowerCase()));
    
    grid.innerHTML = filtered.map(game => {
        const final_price = (game.price * (1 - game.discount / 100)).toFixed(2);
        
        // Mapeo de plataformas a iconos Font Awesome
        const platformIcons = {
            'PC (Steam)': '<i class="fab fa-steam"></i>',
            'PlayStation': '<i class="fab fa-playstation"></i>',
            'Xbox': '<i class="fab fa-xbox"></i>',
            'Nintendo': '<i class="fas fa-gamepad"></i>'
        };
        
        const platformIcon = platformIcons[game.platform] || '<i class="fas fa-desktop"></i>';
        
        return `
            <article class="item" data-id="${game.id}">
                <a class="cover" href="#">
                    <picture>
                        <img src="${game.image_url}" alt="${game.name}" loading="lazy"
                             onerror="this.src='https://via.placeholder.com/380x218?text=No+Image'">
                    </picture>
                    ${game.discount > 0 ? `<span class="discount">-${game.discount}%</span>` : ''}
                    <div class="game-card-actions">
                        <button class="btn-edit" onclick="event.preventDefault(); edit_game(${game.id})"><i class="fas fa-pen"></i></button>
                        <button class="btn-delete" onclick="event.preventDefault(); delete_game(${game.id})"><i class="fas fa-trash"></i></button>
                    </div>
                </a>
                <div class="information">
                    <div class="text">
                        <span class="platform">${platformIcon} ${game.platform}</span>
                        <div class="name">
                            <span class="title">${game.name}</span>
                        </div>
                        <span class="price">${final_price} €</span>
                    </div>
                </div>
            </article>
        `;
    }).join('');
}

function update_hero() {
    if (games.length === 0) return;
    
    // Buscar Cyberpunk 2077 o usar el primer juego
    const featured = games.find(g => g.name === 'Cyberpunk 2077') || games[0];
    const final_price = (featured.price * (1 - featured.discount / 100)).toFixed(2);
    
    document.getElementById('hero-title').textContent = featured.name;
    document.getElementById('hero-discount').textContent = `-${featured.discount}%`;
    document.getElementById('hero-price').textContent = `${final_price} €`;
    document.getElementById('hero-bg').style.backgroundImage = `url(${featured.image_url})`;
}

function open_modal(title = 'Añadir Juego') {
    document.getElementById('modal-title').textContent = title;
    document.getElementById('modal-admin').classList.add('active');
}

function close_modal() {
    document.getElementById('modal-admin').classList.remove('active');
    document.getElementById('form-game').reset();
    document.getElementById('game-id').value = '';
}

async function edit_game(id) {
    const game = games.find(g => g.id === id);
    if (!game) return;
    
    document.getElementById('game-id').value = game.id;
    document.getElementById('game-name').value = game.name;
    document.getElementById('game-platform').value = game.platform;
    document.getElementById('game-price').value = game.price;
    document.getElementById('game-discount').value = game.discount;
    document.getElementById('game-image').value = game.image_url;
    
    open_modal('Editar Juego');
}

async function delete_game(id) {
    if (!confirm('¿Eliminar este juego?')) return;
    
    try {
        const response = await fetch(`${api_url}/${id}`, { method: 'DELETE' });
        if (response.ok) {
            load_games();
        }
    } catch (error) {
        console.error('Error eliminando:', error);
    }
}

async function save_game(e) {
    e.preventDefault();
    
    const id = document.getElementById('game-id').value;
    const data = {
        name: document.getElementById('game-name').value,
        platform: document.getElementById('game-platform').value,
        price: parseFloat(document.getElementById('game-price').value),
        discount: parseInt(document.getElementById('game-discount').value) || 0,
        image_url: document.getElementById('game-image').value
    };
    
    try {
        const url = id ? `${api_url}/${id}` : api_url;
        const method = id ? 'PUT' : 'POST';
        
        const response = await fetch(url, {
            method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            close_modal();
            load_games();
        } else {
            const error = await response.json();
            alert(error.detail || 'Error guardando');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

document.getElementById('btn-add-game').addEventListener('click', () => open_modal());
document.getElementById('btn-close-modal').addEventListener('click', close_modal);
document.getElementById('btn-cancel').addEventListener('click', close_modal);
document.getElementById('form-game').addEventListener('submit', save_game);

document.querySelectorAll('.platform-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        document.querySelectorAll('.platform-link').forEach(l => l.classList.remove('active'));
        link.classList.add('active');
        current_platform = link.dataset.platform;
        render_games();
    });
});

document.getElementById('modal-admin').addEventListener('click', (e) => {
    if (e.target.id === 'modal-admin') close_modal();
});

load_games();
