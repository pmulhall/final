setUpKeyboardShorcuts: function() {
        Mousetrap.bind("right", function() { cards.positiveResponse(); });
        Mousetrap.bind("left",  function() { cards.negativeResponse(); });
        Mousetrap.bind("up",  function() { cards.replayAudio(); });
      },

this.setUpButtons();
        this.setUpKeyboardShorcuts();

https://craig.is/killing/mice
