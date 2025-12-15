import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";

export default [
  { files: ["**/*.{js,mjs,cjs,ts}"] },
  { languageOptions: { globals: globals.browser } },
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      "no-undef": "error",
      "no-constant-binary-expression": "error",
      "no-dupe-else-if": "error",
      "no-duplicate-imports": "error",
      "no-unused-vars": "error",
      "no-var": "error",
      "no-useless-assignment": "error",
      "func-name-matching": "warn",
      "no-console": "warn",
      "no-empty": "error",
      "no-empty-function": "warn",
      "no-lone-blocks": "warn",
    },
  },
];
