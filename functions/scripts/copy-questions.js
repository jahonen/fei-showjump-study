const fs = require('fs');
const path = require('path');

const src = path.resolve(__dirname, '..', '..', 'questions');
const dest = path.resolve(__dirname, '..', 'questions');

function copyRecursive(srcDir, destDir) {
  fs.mkdirSync(destDir, { recursive: true });
  for (const entry of fs.readdirSync(srcDir, { withFileTypes: true })) {
    const srcPath = path.join(srcDir, entry.name);
    const destPath = path.join(destDir, entry.name);
    if (entry.isDirectory()) {
      copyRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

if (fs.existsSync(src)) {
  copyRecursive(src, dest);
  console.log(`Copied question bank from ${src} to ${dest}`);
} else {
  console.warn(`Question bank not found at ${src}`);
}
