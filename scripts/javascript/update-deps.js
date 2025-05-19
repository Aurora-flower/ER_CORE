// update-deps.js
const { exec } = require("node:child_process")
const { readFileSync } = require("node:fs")

/**
 * 忽略的依赖包 - 版本差异过大，更改后会造成项目崩坏
 * @type {string[]}
 */
const fixedDeps = [
  // 'tailwindcss'
]

const packageJson = readFileSync("package.json", "utf-8")
const packageData = JSON.parse(packageJson)

try {
  const subprocess = exec("npm outdated --json", {
    encoding: "utf-8"
  })

  subprocess.stdout.on("data", data => {
    const outdated = JSON.parse(data)
    const list = Object.keys(outdated)
    const { devDependencies, dependencies } = packageData
    const collectDependencies = list.filter(
      pkg => pkg in dependencies && !fixedDeps.includes(pkg)
    )
    const collectDevDependencies = list.filter(
      pkg => pkg in devDependencies && !fixedDeps.includes(pkg)
    )
    const str_separator = `${"\n".padEnd(50, "*")}\n`
    console.log(
      "%cUpdate all dependencies to the latest version:",
      "color: yellow",
      str_separator,
      collectDependencies.length > 0
        ? `npm install ${collectDependencies.map(pkg => `${pkg}@latest`).join(" ")} --no-save-dev`
        : undefined, // --save
      str_separator,
      collectDevDependencies.length > 0
        ? `npm install ${collectDevDependencies.map(pkg => `${pkg}@latest`).join(" ")} --save-dev`
        : undefined
    )
  })
} catch (error) {
  console.error("Script execution error:", error.status, error.message)
}
