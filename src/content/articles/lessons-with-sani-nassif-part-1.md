---
type: "note"          
title: "Lessons with Sani Nassif, part 1"    
date: 2026-03-12
lang: "zh"
tags: ["engineering", "lesson", "modeling"]
draft: false
---

Sani R. Nassif 博士是美國Radyalis公司創辦人暨執行長，為IEEE終身會士(Life Fellow），曾任 IEEE CEDA 總裁，以及ICCAD 2008 大會主席，亦是 IBM Master Inventor，擁有75 件以上專利，並曾獲 DAC、ICCAD、CICC、ISQED 等頂尖會議的多項最佳論文獎。

這次學校邀請他來上一個為期六周的課程，Sani 是個很純粹的"工程師"和研究學者，講話蠻搞笑的，但蘊含著很多的智慧，我想記錄一下學習到了甚麼。

<div class="styled-quote">
<div class="styled-quote-mark">"</div>
<div class="styled-quote-text">

The most important thing to ask in an interview: How will i be evaluated?

</div>
<div class="styled-quote-source">－ Sani R. Nassif</div>
</div>



## 工程師怎麼解決問題的：MASO framework

Sani認為學校都沒有教我們怎麼解決問題，其實工程師有個很重要解決問題的 framework, **MASO**:
- Modeling (模型)
- Analysis (分析)
- Simulation (模擬)
- Optimization (優化)

Sani 舉了一個很生動的例子：他怎麼優化通勤時間。

假設他要從學校走路去捷運站，要走468公尺，有兩個方面可以優化：他可以走很快，消耗很多能量但省時間；或是他可以慢慢走，省能量但花時間。如何把這個問題變成後續可以分析和模擬的過程，就是 modeling。

要模擬甚麼，剛剛說的時間和能量。時間可以分成走路和等車的時間，用一般的常識和機率可以知道，走路時間就是 $\frac{468}{v}$ ，等車時間假設是600s，那平均期望值是 300s，$T_{total}=\frac{468}{v}+300$

但能量怎麼模擬，我可沒學過走一段路會花多少能量， Sani 也不知道，可是有人知道，上網查會發現有人做過相關研究，會得出一個奇怪的式子，$P_{walk}=\frac{mg}{\pi}\sqrt{ \frac{3gL}{2} }\left( 1-\sqrt{ \frac{\pi^2v^2}{6gL} } \right)$。拿來用就可以了。**工程師遇到不會的事，不用發明新的式子，而是善於搜尋運用已經知道的事實。**

利用這兩個公式，我們可以把他們做線性相加並畫出來，就可以做分析了。Sani 說這是 goodness metric，怎麼設計要看你的目標是甚麼，如果你重視時間多一點，就把他權重加大，反之就減少。

<picture>
  <source srcset="/figures/sani-fig1-goodness-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig1-goodness-light.svg" alt="Goodness Metric">
</picture>


下一步是 Simulation ，因為我們其實不知道我們剛剛跑出來的 goodness metric 到底準不準，模擬之後才可以知道這個 error 是不是我們能接受的。但是模擬的時候，可以想見我們會有很多不確定性，我會不會停下來綁鞋帶，走路會不會忽快忽慢，捷運會不會有誤點等等。這麼多不確定性的時候，我們有個非常好用的數學模型 - [中央極限定理 central limit theorem](https://zh.wikipedia.org/zh-tw/%E4%B8%AD%E5%BF%83%E6%9E%81%E9%99%90%E5%AE%9A%E7%90%86)。彼此獨立的隨機變數加總起來，會呈現常態分佈，這是很好用的工具和直覺。

因此我們把剛剛的分析加上常態分佈後，就更貼近真實的情況，這就是著名的[蒙地卡羅方法 Monte Carlo Method](https://zh.wikipedia.org/zh-tw/%E8%92%99%E5%9C%B0%E5%8D%A1%E7%BE%85%E6%96%B9%E6%B3%95)^[因為發現者烏拉姆的叔叔經常在的蒙地卡羅賭場輸錢得名]

<picture>
  <source srcset="/figures/sani-fig2-montecarlo-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig2-montecarlo-light.svg" alt="Monte Carlo">
</picture>


最後是 optimization，這邊有很多作法，其中一個是 [Karush-Kuhn-Tucker Conditions](https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions)，也就是我們熟知的微分找 0 點的做法。

這大概就是 Sani 說的 MASO 流程，我們挑一個問題，然後用 MASO 處理後，中間會用到一些微積分、代數、統計、數值分析等等工具，缺少的知識就想辦法取得 (Internet and AI are good leverage) ，最後得到感覺差不多對的答案，這好像沒有太難嘛！

當然，真實世界的問題沒有這麼簡單，Sani 接著詳細說明 Modeling 以及可能遇到的問題。
## Modeling

Modeling 最終目的都是為了 simulation，複雜的程度取決你的 simulator 的能力。

拿 resistor 來舉例，我們看到電阻，自然想到的是 V=IR ，分壓公式等這些高中就學過的定理，但是其實我們在心裡已經做了很多假設，但這些不一定是對的。

我們假設電阻符合歐姆定律，所以 V=IR；分壓定理是我們假設電流守恆、電壓守恆 (學過電路學的話是KVL, KCL)；我們假設電線的電阻是零...... 這讓我想到**我們的思考很多時候停留在第一層思考，再往下想下去會發現不見得這麼理所當然。**

> We often forget how complicated things are

尤其在EE，我們可以，有時候也必須問到非常細。電阻怎麼來的，我們可以簡單用歐姆定律解釋，也可以再往下看一點，[德魯德模型 (Drude Model)](https://zh.wikipedia.org/zh-tw/%E5%BE%B7%E9%B2%81%E5%BE%B7%E6%A8%A1%E5%9E%8B) 告訴我們電阻是取決電子在飄移速度有關，飄移速度又跟電子的平均自由時間 (mean free path, 平均隔多久會撞到別人) 有關。我們還可以再往下看，量子力學說電子有波粒二象性，更類似波的干涉和繞射...

Sani 說這是 abstraction layer，我們永遠可以問到更細節，但是我們必須決定要停在哪邊，過高的複雜性讓我們無法模擬。

我們進到實際 modeling，這邊基本上就是，我們有一張圖和很多數據點，要怎麼用一條線把這些點串起來。最簡單的例子是 Linear Regression。我們用 $y=a_{1}x+a_{0}$ 來去 fit 一條直線，目標是把每個點到直線的距離最小化。這邊有個反直覺的就是 Linear 其實是對係數 linear，所以 $y=a_{2}x^2+a_{1}x+a_{0}$ 也是 linear ，甚至可以把 x 做各種變形再丟進去，log, sin都可以。同樣的 y 也可以做一樣的變化後再 fit ，這些都屬於 linear regression。

實作方法可以很簡單的用 python 各種套件，AI可以很輕易地做到了。

<picture>
  <source srcset="/figures/sani-fig4-linreg-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig4-linreg-light.svg" alt="Linear Regression">
</picture>

Sani 特別提醒，plots 可以騙人，要注意看 scale ，更要注意看 residual ，這比那條主要的回歸直線還有用，如果 residual 看起來是兩邊比較高，中間很少，那你可能就會懷疑是不是少一個 $x^2$ 的項。

<picture>
  <source srcset="/figures/sani-fig5-residual-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig5-residual-light.svg" alt="Residual">
</picture>

這邊更 detail 的知識就不贅述了，有興趣的可以去學 [Linear Regression](https://zh.wikipedia.org/zh-tw/%E7%B7%9A%E6%80%A7%E5%9B%9E%E6%AD%B8) 和 [Numerical Analysis](https://zh.wikipedia.org/zh-tw/%E6%95%B0%E5%80%BC%E5%88%86%E6%9E%90)。以下還記了一些 Sani 提到的重點
- 我們在職場中需要 rear protection^[lol] ，像是 safety margin 那樣，給自己一點錯誤的空間，不要凡事都給很確定的答案。
- Engineers need to know just enough math to do their work, not invent new math
- You will get data, they are by nature shitty.

有個小故事我覺得值得提一下，Sani 說了他怎麼在 Bell Lab 幫傳奇的 [Hermann K. Gummel](https://en.wikipedia.org/wiki/Hermann_Gummel) 做 modeling。他們要模擬 [ring oscillator](https://en.wikipedia.org/wiki/Ring_oscillator)^[Sani 說半導體世界可以分成兩端，一端是TSMC這種foundry，一端是apple, NV這種 design house，處在中間的是 ring oscillator，溝通兩邊最重視的timing性能]。Sani 很高興的用剛剛說的方法做出來了，看起來還挺不錯的阿，很漂亮的回歸直線，有一些誤差但似乎不太影響。

<picture>
  <source srcset="/figures/sani-fig3-regression-dark.svg" media="(prefers-color-scheme: dark)">
  <img src="/figures/sani-fig3-regression-light.svg" alt="Regression">
</picture>


Hermann 看到之後，很有禮貌地問道：Good, but **What does your model predict for distance=0 and**
**distance=∞ ?**

仔細看會發現這張圖的回歸直線沒有交於 (0,0)，這顯然不合理，無限大的情況也無法用簡單線性模型來模擬。這個經驗告訴我們，在開始做模擬之前，要先考慮物理性質和極端值，先考慮那些"一定對不能錯的地方"，再開始後面的模擬

> Start from the asymptotes and then refine the model

## Office Hour

之後的課程我會補一些課後去問 Sani 的問題，我盡量每堂課都去問問題。