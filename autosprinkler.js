// ==UserScript==
// @name         Autosprinkler
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  I'm spriiiinkling
// @author       official_techsupport
// @match        https://discord.com/channels/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=discord.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    let wasWaterable = false; // avoid spam when actually unwaterable

    function f() {
        const delay = 5000 + Math.floor(Math.random() * 100);
        setTimeout(f, delay);
        const droplets = document.querySelectorAll('button > div > div > img.emoji[data-name=\uD83D\uDCA7]');
        if (!droplets.length) {
            console.log('No droplets');
            return;
        }
        const button = droplets[droplets.length - 1].parentElement.parentElement.parentElement;
        const comment = button.parentElement.parentElement.parentElement.parentElement;
        const text = comment.innerText;
        const canWater = text.includes('Ready to be watered!');
        console.log(JSON.stringify({wasWaterable, canWater}));
        if (canWater && !wasWaterable) {
            console.log('Watering!');
            button.click();
        }
        wasWaterable = canWater;
    }

    f();
})();
