const selectBtnAno = document.getElementById('filter-ano'),
      selectBtnSexo = document.getElementById('filter-sexo'),
      selectBtnEstabelecimento = document.getElementById('filter-estabelecimento'),
      items = document.querySelectorAll('.item');

selectBtnAno.addEventListener('click', () => {
    selectBtnAno.classList.toggle('open');
});

selectBtnSexo.addEventListener('click', () => {
    selectBtnSexo.classList.toggle('open');
});

selectBtnEstabelecimento.addEventListener('click', () => {
    selectBtnEstabelecimento.classList.toggle('open');
});

items.forEach(item => {
    item.addEventListener('click', () => {
        item.classList.toggle('checked');
    });
});

window.onload = function () {
    document.getElementById('todos-sexo').addEventListener('change', function () {
        var checkboxes = document.getElementsByName('sexos');
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].id != 'todos-sexo') {
                checkboxes[i].checked = this.checked;
            }
        }
    });
    document.getElementById('todos-ano').addEventListener('change', function () {
        var checkboxes = document.getElementsByName('years');
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].id != 'todos-ano') {
                checkboxes[i].checked = this.checked;
            }
        }
    });
    document.getElementById('todos-estabelecimento').addEventListener('change', function () {
        var checkboxes = document.getElementsByName('estabelecimentos');
        for (var i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].id != 'todos-estabelecimento') {
                checkboxes[i].checked = this.checked;
            }
        }
    });
}