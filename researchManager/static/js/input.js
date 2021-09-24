(function() {
   
  'use strict';
   
  $('.mandinnen-domeeting').each(function() {
  var $input = $(this),
  $label = $input.next('.js-sanedemandin'),
  labelVal = $label.html();
   
  $input.on('change', function(element) {
  var dsunoemanek = '';
  if (element.target.value) dsunoemanek = element.target.value.split('\\').pop();
  dsunoemanek ? $label.addClass('has-file').find('.js-dsunoemanek').html(dsunoemanek) : $label.removeClass('has-file').html(labelVal);
  });
  });
  
})();
