(function() {
    'use strict';

    const ATTACK_PATTERNS = ["سقوط وشيك", "حصار خانق", "انسحاب جماعي", "لا مفر", "بيع الجبهات"];

    function scanFeed() {
        const posts = document.querySelectorAll('div[data-ad-preview="message"], div.userContent, div.message, div[role="article"]');

        posts.forEach(post => {
            if (post.dataset.shieldChecked) return;
            post.dataset.shieldChecked = "true";

            const text = post.innerText || "";
            const matchedPattern = ATTACK_PATTERNS.find(pattern => text.includes(pattern));

            if (matchedPattern) {
                applyOverlay(post);
            }
        });
    }

    function applyOverlay(postElement) {
        const overlay = document.createElement('div');
        overlay.style.cssText = `
            background: #111827;
            color: #ffffff;
            padding: 16px;
            border-radius: 8px;
            border-right: 6px solid #ef4444;
            margin: 10px 0;
            font-family: system-ui, sans-serif;
            direction: rtl;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        `;

        overlay.innerHTML = `
            <div style="font-size: 16px; font-weight: bold; color: #f87171; margin-bottom: 8px;">
                🛡️ تم العزل بواسطة درع الوعي: منشور حرب نفسية
            </div>
            <div style="font-size: 14px; color: #d1d5db; line-height: 1.5;">
                <b>الهدف النفسي:</b> إحداث حالة من الرعب والانهيار النفسي في الحاضنة الشعبية.<br>
                <b>الواقع الميداني:</b> الأخبار المنشورة مضللة وغير موثقة ميدانياً.
            </div>
            <button style="margin-top: 12px; background: #374151; color: #fff; border: none; padding: 6px 12px; cursor: pointer; border-radius: 4px; font-size: 12px;" 
                    onclick="this.parentElement.nextElementSibling.style.display='block'; this.parentElement.remove();">
                إظهار المنشور المضلل
            </button>
        `;

        postElement.style.display = 'none';
        postElement.parentNode.insertBefore(overlay, postElement);
    }

    setInterval(scanFeed, 2000);
})();
