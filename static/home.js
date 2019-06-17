$(document).ready(function() {
     $('form').on('submit', function(event) {

       $.ajax({
          data : {
             hypothesis : $('#hypothesis').val(),

             premise: $('#premise').val(),
                 },
             type : 'POST',
             async : true,
             url : '/predict'
            //  success: function(results, textStatus) {                        
            //             console.log("success : ");
            //         },
            // error: function(xhr, status, error)
            // {
            //     console.log("error : " + xhr.responseText);                   
            // }
            }).done(function(results) {
                $('#fwd').text(results.fwd).show()
                
            });
       
      event.preventDefault();
      });
});