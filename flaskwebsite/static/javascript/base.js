$(document).ready(function () {
    var rowsPerPage = 25; // Number of rows to display per page
    var currentPage = 1; // Current page number
    var totalRows = $('.dataframe tbody tr').length; // Total number of rows
  
    // Calculate total number of pages
    var totalPages = Math.ceil(totalRows / rowsPerPage);
  
    // Function to show rows for current page
    function showRows() {
      $('.dataframe tbody tr').hide(); // Hide all rows
      var startIndex = (currentPage - 1) * rowsPerPage; // Calculate starting index
      var endIndex = startIndex + rowsPerPage; // Calculate ending index
      $('.dataframe tbody tr').slice(startIndex, endIndex).show(); // Show rows for current page
    }
  
    // Show initial rows for first page
    showRows();
  
    // Function to update pagination buttons
    function updatePaginationButtons() {
      // Enable/disable previous button
      if (currentPage === 1) {
        $('.pagination button.previous').prop('disabled', true);
      } else {
        $('.pagination button.previous').prop('disabled', false);
      }
  
      // Enable/disable next button
      if (currentPage === totalPages) {
        $('.pagination button.next').prop('disabled', true);
      } else {
        $('.pagination button.next').prop('disabled', false);
      }
    }
  
    // Function to update drop-down menu
    function updateDropdownMenu() {
      // Set drop-down menu value to current rowsPerPage
      $('.dropdown select').val(rowsPerPage);
    }
  
    // Update pagination buttons and drop-down menu on page load
    updatePaginationButtons();
    updateDropdownMenu();
  
    // Event handler for next button
    $('.pagination button.next').on('click', function () {
      if (currentPage < totalPages) {
        currentPage++; // Increment current page
        showRows(); // Show rows for current page
        updatePaginationButtons(); // Update pagination buttons
      }
    });
  
    // Event handler for previous button
    $('.pagination button.previous').on('click', function () {
      if (currentPage > 1) {
        currentPage--; // Decrement current page
        showRows(); // Show rows for current page
        updatePaginationButtons(); // Update pagination buttons
      }
    });
  
    // Event handler for drop-down menu
    $('.dropdown select').on('change', function () {
      rowsPerPage = parseInt($(this).val()); // Update rowsPerPage with selected value
      totalPages = Math.ceil(totalRows / rowsPerPage); // Recalculate total number of pages
      currentPage = 1; // Reset current page to 1
      showRows(); // Show rows for current page
      updatePaginationButtons(); // Update pagination buttons
    });
  });
  