document.addEventListener('DOMContentLoaded', function () {
  const sliders = document.querySelectorAll('.slider');
  const navButtonContainers = document.querySelectorAll('.slider-nav');

  sliders.forEach((slider, index) => {
      const navButtons = navButtonContainers[index].querySelectorAll('a');
      const slideWidth = slider.clientWidth;

      // Set initial active state for the first slide
      navButtons[0].classList.add('active');

      slider.addEventListener('scroll', function () {
          const scrollPosition = slider.scrollLeft;

          navButtons.forEach(function (button, index) {
              const slideOffset = index * slideWidth;
              const isActive = scrollPosition >= slideOffset && scrollPosition < slideOffset + slideWidth;

              if (isActive) {
                  button.classList.add('active');
              } else {
                  button.classList.remove('active');
              }
          });
      });
  });
});

  document.querySelectorAll(".read-more-btn").forEach((button) => {
    button.addEventListener("click", (e) => {
        const textContainer = button.parentElement.querySelector(".text");
        textContainer.classList.toggle("show-more");
        if (button.innerText === "Read More") {
            button.innerText = "Read Less";
        } else {
            button.innerText = "Read More";
        }
    });
});
document.getElementById("surveyForm").addEventListener("submit", function(event) {
    var answers = document.querySelectorAll('input[name^="q"]');
    var answered = true;
    answers.forEach(function(answer) {
        if (!answer.checked) {
            answered = false;
        }
    });
    if (!answered) {
        alert("Please answer all questions before submitting the form.");
        event.preventDefault();
    }
});