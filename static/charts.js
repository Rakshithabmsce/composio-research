document.addEventListener("DOMContentLoaded", function () {

    // DataTable

    if (typeof $ !== "undefined") {

        $("table").DataTable({

            pageLength: 25,

            responsive: true,

            ordering: true,

            searching: true,

            lengthMenu: [10, 25, 50, 100]

        });

    }

    // Verified column coloring

    let rows = document.querySelectorAll("tbody tr");

    rows.forEach(function(row){

        row.innerHTML = row.innerHTML.replace(

            /true/gi,

            '<span class="badge bg-success">Verified</span>'

        );

        row.innerHTML = row.innerHTML.replace(

            /false/gi,

            '<span class="badge bg-danger">Not Verified</span>'

        );

    });

});