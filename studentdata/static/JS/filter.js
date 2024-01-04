//this javascript is use to filter data of attendance, this code filter data by Absent , Present ,Roll No and Range of Date

document.addEventListener('DOMContentLoaded', function (){
    var checkPresent = document.getElementById('checkPresent');
    var checkAbsent = document.getElementById('checkAbsent');
    var startdate = document.getElementById('startdate');
    var enddate = document.getElementById('enddate');
    var filterroll = document.getElementById('filterroll');
    var attendanceTable = document.getElementById('attendanceTable');


    checkPresent.addEventListener('change', applyFilters);
    checkAbsent.addEventListener('change', applyFilters);
    startdate.addEventListener('change', applyFilters);
    enddate.addEventListener('change', applyFilters);
    filterroll.addEventListener('keyup', applyFilters);


    function applyFilters(){
        var showPresent = checkPresent.checked;
        var showAbsent = checkAbsent.checked;
        var showStartdate = startdate.value;
        var showEnddate = enddate.value;
        var filterText = filterroll.value.toUpperCase();
        var anyFiltersSelected = showPresent || showAbsent || (showStartdate && showEnddate) || filterText;


        if (showStartdate && showEnddate && showStartdate > showEnddate) {
            alert("Start date must be Lessthan End date....");
            return;
        }

        for (var i = 1; i < attendanceTable.rows.length; i++){
            var row = attendanceTable.rows[i];
            var attendanceCell = row.cells[2].textContent;
            var dateCell = row.cells[1].textContent;
            var rollNoCell = row.cells[0].textContent.toUpperCase();
            var showRow = filterByCheckbox(attendanceCell, showPresent, showAbsent) && filterByDate(dateCell, showStartdate, showEnddate) && filterByRollNo(rollNoCell, filterText);
            row.style.display = showRow ? '' : 'none';
        }
    }


    function filterByCheckbox(attendanceCell, showPresent, showAbsent){
        return (!showPresent || attendanceCell === 'Present') && (!showAbsent || attendanceCell === 'Absent');
    }


    function filterByDate(dateCell, showStartdate, showEnddate){
        if (!showStartdate && !showEnddate){
            return true;
        }
        var currentDate = new Date(dateCell);
        var startDate = showStartdate ? new Date(showStartdate) : null;
        var endDate = showEnddate ? new Date(showEnddate) : null;

        return (!startDate || currentDate >= startDate) && (!endDate || currentDate <= endDate);
    }


    function filterByRollNo(rollNoCell, filterText){
        return !filterText || rollNoCell.indexOf(filterText) > -1;
    }
});