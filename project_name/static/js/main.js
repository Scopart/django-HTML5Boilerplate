window.app = {};

(function($, document) {
  app.tab = {
    init: function(callback) {
      var id;
      callback = callback || function(tab) {};

      // fix height
      $('[data-tab] > dd > a').css({
        'height': $('[data-tab] > dd').height(),
        'line-height': $('[data-tab] > dd').height() + 'px',
        'vertical-align': 'middle'
      });

      // Handle click and focus
      $(document).on('click focus', '[data-tab] > dd > a', function(e) {
        e.preventDefault();
        var tab = $(this).parent(),
          tabs = tab.closest('[data-tab]'),
          target = $('#' + this.href.split('#')[1]),
          siblings = tab.siblings();

        tab.addClass('active').trigger('opened');
        siblings.removeClass('active');
        target.siblings().removeClass('active').end().addClass('active');
        callback(tab);
        tabs.trigger('toggled', [tab]);
      });
    }
  };
})(jQuery, this.document);