$(document).ready(() => {
  let buttonColors = ["red", "blue", "green", "yellow"];
  let gamePattern = [];
  let userClickedPattern = [];
  let level = 0;

  $("body").one("keydown", function () {
    $("h1").text("level " + level);
    nextSequence();
    userAnswer();
  });
  //   user input ↓↓↓↓
  function userAnswer() {
    $(".btn").on("click", function () {
      let userChosenColor = $(this).attr("id");
      userClickedPattern.push(userChosenColor);
      animatePress(userChosenColor);
      checkAnswer(userClickedPattern[userClickedPattern.length - 1]);
      playSound(userChosenColor);
    });
  }
  function nextSequence() {
    let randomNumber = Math.floor(Math.random() * 4);
    let randomChosenColor = buttonColors[randomNumber];
    let chosenButton = $("." + randomChosenColor);
    gamePattern.push(randomChosenColor);
    chosenButton.fadeOut(100).fadeIn(100);
    playSound(randomChosenColor);
    level += 1;
    $("h1").text("level " + level);
  }

  function playSound(name) {
    let buttonAudio = new Audio("sounds/" + name + ".mp3");
    buttonAudio.play();
  }
  function animatePress(currentColor) {
    $("." + currentColor).addClass("pressed");
    setTimeout(function () {
      $("." + currentColor).removeClass("pressed");
    }, 100);
  }
  function checkAnswer(currentLevel) {
    if (currentLevel === gamePattern[gamePattern.length - 1]) {
      if (userClickedPattern.length === gamePattern.length) {
        userClickedPattern = [];
        setTimeout(function () {
          nextSequence();
        }, 1000);
      }
    } else {
      let wrongAudio = new Audio("sounds/wrong.mp3");
      wrongAudio.play();
      $("body").addClass("game-over");
      setTimeout(() => {
        $("body").removeClass("game-over");
      }, 200);
      $("h1").text("Game Over, Press Any Key to Restart");
      startOver();
      location.reload();
    }
  }
  function startOver() {
    level = 0;
    gamePattern = 0;
  }
});
