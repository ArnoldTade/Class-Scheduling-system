$(document).ready(function () {
  $("#news-slider").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    responsive: {
      0: {
        items: 1,
      },
      600: {
        items: 2,
      },
      1000: {
        items: 3,
      },
    },
  });
});


// CAROUSEL
// CAROUSEL
var $owl = $('.owl-carousel');

$owl.children().each(function (index) {
  $(this).attr('data-position', index); // NB: .attr() instead of .data()
});

$owl.owlCarousel({
  center: true,
  loop: true,
  items: 5,
});

$(document).on('click', '.owl-item>div', function () {
  // see https://owlcarousel2.github.io/OwlCarousel2/docs/api-events.html#to-owl-carousel
  var $speed = 300;  // in ms
  $owl.trigger('to.owl.carousel', [$(this).data('position'), $speed]);
});


// END CAROUSEL
// END CAROUSEL

// Profile Tab //
document.addEventListener('DOMContentLoaded', function () {
  const tabs = document.querySelectorAll(".profile-tab");

  tabs.forEach(tab => {
    tab.addEventListener('click', function (event) {
      event.preventDefault();

      const targetId = this.getAttribute('href').substring(1);
      const targetSection = document.getElementById(targetId);

      if (targetSection) {
        const visibleSection = document.querySelector('.container-tab .visible');
        if (visibleSection) {
          visibleSection.classList.add('invisible');
          visibleSection.classList.remove('visible');
        }
        targetSection.classList.remove('invisible');
        targetSection.classList.add('visible');
      }
    });
  });
});
// End Profile Tab //
