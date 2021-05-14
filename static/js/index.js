new Glide('#banner_slider',{
    type: 'slider',
    startAt: 0,
    perView: 1,
    gap: 20,
    bound: true,
}).mount()

new Glide('#new-arriwal-slider',{
    type: 'slider',
    startAt: 0,
    perView: 2,
    gap: 20,
    bound: true,
    breakpoints: {
        600: { perView: 1 },
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
        600: { perView: 1 },
        1200: { perView: 1 }
    },
}).mount()


new Glide('#gas_boilers_slider',{
    type: 'slider',
    startAt: 0,
    perView: 4,
    gap: 20,
    breakpoints: {
        768: { perView: 1 },
        992: { perView:2},
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
        768: { perView: 1 },
        992: { perView:2},
        1200: { perView: 3 }
    },
    bound: true
}).mount()