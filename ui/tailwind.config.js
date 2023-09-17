module.exports = {
	content: ["./*.html"],
	theme: {
		extend: {
			colors: {
				color_logo: "#50C878",
				color_header: "#E74538",
				color_paragraph: "#FF0080",
			},

			fontFamily: {
				main_header: ["Jost", "sans-serif"],
				logo: ["Space Grotesk", "sans-serif"],
				general: ["Alata", "sans-serif"],
				headers: ["Work Sans", "sans-serif"],
			},

			keyframes: {
				fadein: {
					"0%": {
						opacity: 0,
					},

					"100%": {
						opacity: 1,
					},
				},
			},

			animation: {
				fadein: "fadein 1.5s ease-in-out",
			},
		},
	},
	plugins: [],
};
