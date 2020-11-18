module.exports = {
	future: {
		// removeDeprecatedGapUtilities: true,
		purgeLayersByDefault: true,
	},
	purge: {
		enabled: true,
		content: ["./templates/**/*.html"],
	},
	theme: {
		extend: {},
	},
	variants: {},
	plugins: [],
};
