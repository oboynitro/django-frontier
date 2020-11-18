module.exports = {
	future: {
		// removeDeprecatedGapUtilities: true,
		purgeLayersByDefault: true,
	},
	purge: {
		enabled: true,
		content: ["./resources/css/**/*.css"],
	},
	theme: {
		extend: {},
	},
	variants: {},
	plugins: [],
};
