$(document).ready(function() {
		// JQuery code to be added in here.

    // function for search patients
    $('#searchpatient').keyup(function(){
            var query = $(this).val();
            $.get('/clinic/patients/search/', {p: query}, function(data){
             $('#pats').html(data);
            });
    });

    // calculate age fuction
    $("#id_Date_Naissance").change(function(){
        var mdate = $("#id_Date_Naissance").val().toString();
        var dayThen = parseInt(mdate.substring(0,2), 10);
        var monthThen = parseInt(mdate.substring(3,5), 10);
        var yearThen = parseInt(mdate.substring(6,10), 10);

        var today = new Date();
        var birthday = new Date(yearThen, monthThen-1, dayThen);

        var differenceInMilisecond = today.valueOf() - birthday.valueOf();

        var year_age = Math.floor(differenceInMilisecond / 31536000000);
        var day_age = Math.floor((differenceInMilisecond % 31536000000) / 86400000);

        if ((today.getMonth() == birthday.getMonth()) && (today.getDate() == birthday.getDate())) {
            alert("Happy B'day!!!");
        }

        var month_age = Math.floor(day_age/30);

        day_age = day_age % 30;

        if (isNaN(year_age) || isNaN(month_age) || isNaN(day_age)) {
            $("#id_Age").val("Invalid birthday - Please try again!");
        }
        else {
            if (year_age == 0){
                $("#id_Age").val(month_age + " MOIS");
            }
            else {
                $("#id_Age").val(year_age + " ANS");
            }
        }
    });

    // new goes here

});