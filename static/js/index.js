new Glide('.left-side-sliders',{
    type: 'slider',
    startAt: 0,
    perView: 2,
    gap: 20,
    bound: true,
    breakpoints: {
        600: { perView: 2 },
        1200: { perView: 1 }
    },
}).mount()

new Glide('#top-slider',{
    type: 'slider',
    startAt: 0,
    perView: 2,
    gap: 20,
    bound: true,
    breakpoints: {
        600: { perView: 2 },
        1200: { perView: 1 }
    },
}).mount()

new Glide('.store-box__slider',{
    type: 'slider',
    startAt: 0,
    perView: 4,
    gap: 20,
    breakpoints: {
        600: { perView: 2 },
        1200: { perView: 3 }
    },
    bound: true,
}).mount()

new Glide('#gas_gorel_slider',{
    type: 'slider',
    startAt: 0,
    perView: 4,
    gap: 20,
    breakpoints: {
        600: { perView: 2 },
        1200: { perView: 3 }
    },
    bound: true
}).mount()