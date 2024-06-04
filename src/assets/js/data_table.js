document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');

    document.querySelectorAll('.expand-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var cellContent = btn.previousElementSibling;
            if (cellContent.classList.contains('expanded')) {
                cellContent.classList.remove('expanded');
                btn.innerHTML = '<span class="tf-icons bx bx-plus-circle"></span>';  // 更改按钮内容
            } else {
                cellContent.classList.add('expanded');
                btn.innerHTML = '<span class="tf-icons bx bx-chevron-up"></span>';  // 更改按钮内容
            }
        });
    });
});

const c = document.querySelector('.container');
const indexs = Array.from(document.querySelectorAll('.index'));
let cur = -1;
indexs.forEach((index, i) => {
  index.addEventListener('click', (e) => {
    console.log(`Index ${i + 1} clicked`);  // 添加日志
    // clear
    c.className = 'container';
    void c.offsetWidth; // Reflow
    c.classList.add('open');
    c.classList.add(`i${i + 1}`);
    if (cur > i) {
      c.classList.add('flip');
    }
    cur = i;
  });
});
