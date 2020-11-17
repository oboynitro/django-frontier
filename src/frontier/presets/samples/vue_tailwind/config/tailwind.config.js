module.exports = {
	future: {
		// removeDeprecatedGapUtilities: true,
		purgeLayersByDefault: true,
	},
	purge: {
		enabled: true,
		content: ["./resources/css/**/*.css", "./resources/js/**/*.js"],
	},
	theme: {
		extend: {},
	},
	variants: {},
	plugins: [],
};
