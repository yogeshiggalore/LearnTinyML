// ===== State =====
let modulesData = [];
let currentModule = null;

// ===== Init =====
document.addEventListener("DOMContentLoaded", () => {
    fetchModules();
    handleHash();
    window.addEventListener("popstate", handleHash);
});

// ===== API =====
async function fetchModules() {
    const res = await fetch("/api/modules");
    modulesData = await res.json();
    renderCards(modulesData);
}

async function fetchModuleDetail(slug) {
    const res = await fetch(`/api/modules/${slug}`);
    if (!res.ok) return;
    const data = await res.json();
    currentModule = slug;
    renderDetail(data);
    showDetail();
    updateActiveNav(slug);
}

// ===== Navigation =====
function navigate(slug) {
    if (slug) {
        window.location.hash = slug;
        fetchModuleDetail(slug);
    } else {
        history.pushState(null, "", window.location.pathname);
        currentModule = null;
        showOverview();
        updateActiveNav(null);
    }
    closeNav();
    window.scrollTo({ top: 0, behavior: "smooth" });
}

function handleHash() {
    const hash = window.location.hash.replace("#", "");
    if (hash && ["tinyvox", "tinyvue", "tinyvibe"].includes(hash)) {
        fetchModuleDetail(hash);
    } else {
        showOverview();
        updateActiveNav(null);
    }
}

function showOverview() {
    document.getElementById("hero").classList.remove("hidden");
    document.getElementById("module-detail").classList.add("hidden");
}

function showDetail() {
    document.getElementById("hero").classList.add("hidden");
    document.getElementById("module-detail").classList.remove("hidden");
    document.getElementById("module-detail").classList.add("fade-in");
}

function updateActiveNav(slug) {
    document.querySelectorAll(".nav-link").forEach(link => {
        link.classList.remove("active");
        if (!slug && !link.dataset.module) link.classList.add("active");
        if (slug && link.dataset.module === slug) link.classList.add("active");
    });
}

function toggleNav() {
    document.getElementById("navLinks").classList.toggle("open");
}

function closeNav() {
    document.getElementById("navLinks").classList.remove("open");
}

// ===== Render Cards =====
function renderCards(modules) {
    const container = document.getElementById("moduleCards");
    container.innerHTML = modules.map(m => `
        <div class="module-card" onclick="navigate('${m.slug}')">
            <div class="card-accent" style="background: ${m.color}"></div>
            <div class="card-body">
                <div class="card-domain" style="color: ${m.color}">${m.domain}</div>
                <div class="card-name">${m.name}</div>
                <div class="card-tagline">"${m.tagline}"</div>
                <div class="card-desc">${m.description}</div>
                <div class="card-cta" style="color: ${m.color}">
                    Explore course <span>&rarr;</span>
                </div>
            </div>
        </div>
    `).join("");
}

// ===== Render Detail =====
function renderDetail(data) {
    const color = data.color;

    // Header
    document.getElementById("moduleHeader").innerHTML = `
        <div class="detail-domain" style="color: ${color}">${data.domain}</div>
        <h1 style="color: ${color}">${data.name}</h1>
        <div class="detail-tagline">"${data.tagline}"</div>
        <div class="detail-book" style="border-left-color: ${color}">
            Book: <em>${data.book_title}</em>
        </div>
        <div class="detail-desc">${data.description}</div>
    `;

    // BOM
    document.getElementById("hwSummary").textContent = data.hardware.summary;
    document.getElementById("hwSummary").style.borderLeftColor = color;

    document.getElementById("bomBody").innerHTML = data.hardware.bom.map((item, i) => `
        <tr>
            <td>${i + 1}</td>
            <td><strong>${item.component}</strong></td>
            <td>${item.description}</td>
            <td>${item.qty}</td>
            <td>${item.interface}</td>
        </tr>
    `).join("");

    document.getElementById("hwNotes").innerHTML = data.hardware.notes.map(note => `
        <li>${note}</li>
    `).join("");

    // Outline
    document.getElementById("outlineContent").innerHTML = data.outline.map(part => `
        <div class="part-block">
            <details>
                <summary style="border-left-color: ${color}">${part.part}</summary>
                <div class="part-chapters">
                    ${part.chapters.map(ch => `
                        <div class="chapter-block">
                            <details>
                                <summary>${ch.title}</summary>
                                <ul class="section-list">
                                    ${ch.sections.map(s => `<li>${s}</li>`).join("")}
                                </ul>
                            </details>
                        </div>
                    `).join("")}
                </div>
            </details>
        </div>
    `).join("");
}
