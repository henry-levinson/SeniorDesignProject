$(document).ready(function () {
    // Initialize star icons
    $(document).on('click', '.star', function() {
      $(this).addClass('active');
      $(this).prevAll('.star').addClass('active');
      $(this).nextAll('.star').removeClass('active');
      $(this).siblings('.star').attr('data-rating', '0');
      $(this).attr('data-rating', '1');
      
      // Get the row index and ranking value
      var rowIndex = $(this).closest('tr').index();
      var ranking = $(this).index() + 1;
      
      // Save the ranking in local storage
      localStorage.setItem('ranking_' + rowIndex, ranking);
    });
    
    // Load saved rankings from local storage
    $('.star').each(function() {
      var rowIndex = $(this).closest('tr').index();
      var savedRanking = localStorage.getItem('ranking_' + rowIndex);
      if (savedRanking) {
        $(this).siblings('.star').removeClass('active');
        $(this).removeClass('active');
        $(this).siblings('.star').attr('data-rating', '0');
        $(this).attr('data-rating', savedRanking);
        $(this).prevAll('.star').addClass('active');
      }
    });
    
    // Reset star icons
    $('.stars').mouseleave(function() {
      $(this).find('.star').removeClass('active');
      $(this).find('.star').attr('data-rating', '0');
    });
  });
  