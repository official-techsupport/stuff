// ==UserScript==
// @name         Autosprinkler
// @namespace    http://tampermonkey.net/
// @version      0.2
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
        const canWater = text.includes('\nReady to be watered!\n');
        console.log(JSON.stringify({wasWaterable, canWater}));
        if (canWater && !wasWaterable) {
            console.log('Watering!');
            button.click();
        }
        wasWaterable = canWater;

        const clickies = document.querySelectorAll('a[role=button]');
        for (const it of clickies) {
            if (it.innerText == 'Dismiss message') {
                console.log('Dismissing: ' + it.parentElement.parentElement.innerText.split(/\n/)[0]);
                it.click();
            }
        }
    }

    f();
})();
