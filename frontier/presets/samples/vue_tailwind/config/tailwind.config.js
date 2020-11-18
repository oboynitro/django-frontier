module.exports = {
	future: {
		// removeDeprecatedGapUtilities: true,
		purgeLayersByDefault: true,
	},
	purge: {
		enabled: true,
		content: [
			"./resources/css/**/*.css",
			"./resources/js/**/*.js",
			"./resources/js/**/*.vue",
			"./templates/**/*.html",
		],
	},
	theme: {
		extend: {},
	},
	variants: {},
	plugins: [],
};
