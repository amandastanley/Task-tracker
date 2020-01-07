function displayData (data) {
    // append everything...
          // OR, work with a list in JS
        var $tl = $('<div class="tasks"></div>')
        $('.thingsihaveputin').html('')
        $('.thingsihaveputin').append($tl)
        data.items.forEach(
          function (item) {
            $tl.append(
               $( `
            <div class="item">
                <div class="left">
                  ${item.task}
                </div>
                <div class="middle">
                  ${item.duedate}
                </div>
                <div class="right">
                  ${item.budget}
                </div> 
            </div>  
                `)
            )
          }
        )
          
}


// when the document is ready
$(document).ready( 
  // do this...
  function () { 

    // load test data...
    $.ajax({
      type:'GET',
      url:'/test/json',
      success: displayData,
    })


    $("#formthing").submit(function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);
    var url = form.attr('action');

    $.ajax({
           type: "POST",
           url: url,
           data: form.serialize(), // serializes the form's elements.
           success: displayData,
         });


});
  }


);