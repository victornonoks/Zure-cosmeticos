// Módulo de uso para o GSAP

 document.addEventListener("DOMContentLoaded", (event) => {
    let smoother = ScrollSmoother.create({
    smooth: 2,   // seconds it takes to "catch up" to native scroll position
    effects: true // look for data-speed and data-lag attributes on elements and animate accordingly
    });

  gsap.registerPlugin(ScrollTrigger,ScrollSmoother)
  // gsap code here!

    gsap.from(".titulo-banner", {
        x: -200,
        delay: 0.3,
        opacity: 0,    
    });

    gsap.from(".paragrafo-banner", {
        y: 100,
        delay: 0.5,
        opacity: 0,
    });

    gsap.from(".btn-banner", {
        y: 100,
        delay: 0.8,
        opacity: 0
    });

    gsap.from(".titulo-sobre", {
        scrollTrigger: {
            trigger: '.titulo-sobre',
            toggleActions: 'restart',
            end: 'top 50%',
            scrub: true,
        },
        y: 100,
        opacity: 0,
    });

    gsap.from(".p-sobre", {
        scrollTrigger: {
            trigger: ".p-sobre",  
            toggleActions: 'restart', 
            end: 'top 50%',
            scrub:  true
        },
        y: 100,
        opacity: 0,
    })

    gsap.from(".titulo-destaques", {
        scrollTrigger: {
            trigger: ".titulo-destaques",
            toggleActions: "restart",
            end: "bottom 40%",
            scrub: true
        },
        y: 80, 
        opacity: 0,
    })

    gsap.from(".produtos-destaques", {
        scrollTrigger: {
            trigger: ".produtos-destaques",
            toggleActions: "restart",
            end: "top 50%",  
            scrub: 1,
        },
        y: 100,
        opacity: 0,
        duration: 1,
    })

    gsap.from(".titulo-video", {
        scrollTrigger: {
            trigger: ".titulo-video",
            toggleActions: "restart",
            end: "top 60%",
            scrub: 1,
        },
        x: -300,
        opacity:0,
    })

        gsap.from(".texto-video", {
        scrollTrigger: {
            trigger: ".texto-video",
            toggleActions: "restart",
            end: "top 60%",
            scrub: 1,
        },
        x: -300,
        opacity:0,
    })

        gsap.from(".lista-video", {
        scrollTrigger: {
            trigger: ".lista-video",
            toggleActions: "restart",
            end: "top 70%",
            scrub: 1,
        },
        x: -300,
        opacity:0,
    })

    gsap.from(".video", {
        scrollTrigger: {
            trigger: ".video",
            toggleActions: "restart",
            end: "top 20%",
            scrub:1,
        },
        x: 300,
        opacity: 0
    })

    gsap.from(".produtos-texto", {
        scrollTrigger: {
            trigger: ".produtos-texto",
            toggleActions: "restart",
            end: "top 50%",
            scrub: 1,
        },
        y: 100,
        opacity:0
    })

    gsap.from(".produtos", {
        scrollTrigger: {
            trigger: ".produtos",
            toggleActions: "restart",
            end: "top 50%",  
            scrub: 1,
        },
        y: 100,
        opacity: 0,
        duration: 1,
    })
 });