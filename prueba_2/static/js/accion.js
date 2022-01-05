$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "position"},
            {"data": "relatoUsuario"},
        ],
//        columnDefs: [
//            {
//                targets: [-2],
//                class: 'text-center',
//                orderable: false,
//                render: function (data, type, row) {
//                    return '<p>Esto es una prueba</p>';
//                }
//            },
//        ],
        initComplete: function (settings, json) {

        }
    });

});