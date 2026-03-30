// Biến toàn cục lưu dữ liệu
let problemsData = [];

document.addEventListener('DOMContentLoaded', () => {
    initThemeToggle();

    // Routing đơn giản dựa trên DOM
    if (document.getElementById('problems-table-body')) {
        initHome();
    } else if (document.getElementById('problem-title')) {
        initDetail();
    }
});

/* =========================================
   GIAO DIỆN & DARK MODE
========================================= */
function initThemeToggle() {
    const toggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateBtnText(toggleBtn, currentTheme);

    toggleBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateBtnText(toggleBtn, newTheme);
    });
}

function updateBtnText(btn, theme) {
    if(!btn) return;
    btn.textContent = theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode';
}

/* =========================================
   TRANG CHỦ (INDEX.HTML)
========================================= */
async function initHome() {
    try {
        const response = await fetch('data/problems.json');
        problemsData = await response.json();
        renderTable(problemsData);
        setupFilters();
    } catch (error) {
        console.error('Lỗi khi tải dữ liệu bài tập:', error);
        document.getElementById('problems-table-body').innerHTML = 
            '<tr><td colspan="4" style="text-align:center; color:red;">Không thể tải dữ liệu. Vui lòng kiểm tra lại.</td></tr>';
    }
}

function renderTable(data) {
    const tbody = document.getElementById('problems-table-body');
    tbody.innerHTML = '';

    if (data.length === 0) {
        tbody.innerHTML = '<tr><td colspan="4" style="text-align:center;">Không tìm thấy bài toán nào phù hợp.</td></tr>';
        return;
    }

    data.forEach(p => {
        const tr = document.createElement('tr');
        
        // Cột Tên bài
        const tdName = document.createElement('td');
        const link = document.createElement('a');
        link.href = `problem.html?id=${p.id}`;
        link.textContent = p.title;
        link.className = 'problem-link';
        tdName.appendChild(link);

        // Cột Chủ đề
        const tdTopic = document.createElement('td');
        p.topics.forEach(topic => {
            const span = document.createElement('span');
            span.className = 'topic-tag';
            span.textContent = topic;
            tdTopic.appendChild(span);
        });

        // Cột Độ khó
        const tdDiff = document.createElement('td');
        const diffBadge = document.createElement('span');
        diffBadge.className = `diff-badge diff-${p.difficulty}`;
        diffBadge.textContent = `⭐ ${p.difficulty}`;
        tdDiff.appendChild(diffBadge);

        // Cột Nguồn
        const tdSource = document.createElement('td');
        tdSource.textContent = p.source;

        tr.appendChild(tdName);
        tr.appendChild(tdTopic);
        tr.appendChild(tdDiff);
        tr.appendChild(tdSource);
        tbody.appendChild(tr);
    });
}

function setupFilters() {
    const searchInput = document.getElementById('search-input');
    const topicFilter = document.getElementById('topic-filter');
    const diffFilter = document.getElementById('diff-filter');
    const sortFilter = document.getElementById('sort-filter');

    const applyFilters = () => {
        let filtered = problemsData.filter(p => {
            const matchSearch = p.title.toLowerCase().includes(searchInput.value.toLowerCase()) || 
                                p.tags.some(tag => tag.toLowerCase().includes(searchInput.value.toLowerCase()));
            const matchTopic = topicFilter.value === 'all' || p.topics.includes(topicFilter.value);
            const matchDiff = diffFilter.value === 'all' || p.difficulty == diffFilter.value;
            
            return matchSearch && matchTopic && matchDiff;
        });

        // Sorting
        const sortVal = sortFilter.value;
        if (sortVal === 'diff-asc') {
            filtered.sort((a, b) => a.difficulty - b.difficulty);
        } else if (sortVal === 'diff-desc') {
            filtered.sort((a, b) => b.difficulty - a.difficulty);
        } else if (sortVal === 'name-asc') {
            filtered.sort((a, b) => a.title.localeCompare(b.title));
        }

        renderTable(filtered);
    };

    searchInput.addEventListener('input', applyFilters);
    topicFilter.addEventListener('change', applyFilters);
    diffFilter.addEventListener('change', applyFilters);
    sortFilter.addEventListener('change', applyFilters);
    
    // Default sort run
    applyFilters();
}

/* =========================================
   TRANG CHI TIẾT (PROBLEM.HTML)
========================================= */
async function initDetail() {
    const urlParams = new URLSearchParams(window.location.search);
    const problemId = urlParams.get('id');

    if (!problemId) {
        document.getElementById('problem-title').textContent = 'Lỗi: Không tìm thấy ID bài toán';
        return;
    }

    try {
        const response = await fetch('data/problems.json');
        const data = await response.json();
        const problem = data.find(p => p.id === problemId);

        if (problem) {
            document.getElementById('problem-title').textContent = problem.title;
            document.title = `${problem.title} - Olympiad Library`;
            document.getElementById('problem-complexity').textContent = problem.complexity;
            
            const diffBadge = document.createElement('span');
            diffBadge.className = `diff-badge diff-${problem.difficulty}`;
            diffBadge.textContent = `Mức độ ${problem.difficulty}`;
            document.getElementById('problem-difficulty').innerHTML = '';
            document.getElementById('problem-difficulty').appendChild(diffBadge);

            const tagsContainer = document.getElementById('problem-tags');
            problem.tags.forEach(tag => {
                const tagSpan = document.createElement('span');
                tagSpan.className = 'topic-tag tag-sm';
                tagSpan.textContent = `#${tag}`;
                tagsContainer.appendChild(tagSpan);
            });

          

            // --- XỬ LÝ NÚT CHẤM ONLINE VÀ CODE SINH TEST ---
            const extraContainer = document.getElementById('extra-resources');
            extraContainer.innerHTML = ''; // Xóa nút cũ nếu có

            // Nút chấm bài online
            if (problem.judge_url) {
                const judgeBtn = document.createElement('a');
                judgeBtn.href = problem.judge_url;
                judgeBtn.className = 'btn outline secondary extra-btn';
                judgeBtn.textContent = '🚀 Nộp bài Online';
                judgeBtn.target = '_blank'; // Mở tab mới
                judgeBtn.rel = 'noopener noreferrer'; // Bảo mật khi mở tab mới
                extraContainer.appendChild(judgeBtn);
            }

            // Nút tải/xem code sinh test (Python/C++)
            if (problem.generator) {
                const genBtn = document.createElement('a');
                genBtn.href = problem.generator;
                genBtn.className = 'btn outline secondary extra-btn';
                genBtn.textContent = '⚙️ Code sinh Test';
                genBtn.target = '_blank';
                // Thêm thuộc tính download nếu bạn muốn ép trình duyệt tải file về thay vì hiển thị code
                // genBtn.download = ''; 
                extraContainer.appendChild(genBtn);
            }
            // ----------------------------------------------

            const iframe = document.getElementById('solution-iframe');
            iframe.src = problem.solution;

            document.getElementById('open-full-btn').addEventListener('click', () => {
                window.open(problem.solution, '_blank');
            });
        } else {
            document.getElementById('problem-title').textContent = 'Bài toán không tồn tại';
        }
    } catch (error) {
        console.error('Lỗi tải chi tiết:', error);
    }
}
