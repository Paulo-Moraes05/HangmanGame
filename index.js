import fs from "fs";

const sbom = JSON.parse(fs.readFileSync("sbom.json", "utf8"));

for (const comp of sbom.components || []) {
  comp.properties = comp.properties || [];

  const hasArchiveProp = (comp.properties || []).find(
    (p) => p.value?.endsWith(".tgz") ||
      p.value?.toLowerCase().endsWith(".tar") ||
      p.value?.toLowerCase().endsWith(".zip") ||
      p.value?.toLowerCase().endsWith(".arc")
  );

  const hasExecutableProp = (comp.properties || []).find(
    (p) => p.value?.toLowerCase().endsWith(".exe") ||
      p.value?.toLowerCase().endsWith(".apk") ||
      p.value?.toLowerCase().endsWith(".app") ||
      p.value?.toLowerCase().endsWith(".scr")
  );

  const hasStructureProp = (comp.properties || []).find(
    (p) => p.value?.toLowerCase().endsWith(".csv") ||
      p.value?.toLowerCase().endsWith(".json") ||
      p.value?.toLowerCase().endsWith(".ini") ||
      p.value?.toLowerCase().endsWith(".yml") ||
      p.value?.toLowerCase().endsWith(".xml") ||
      p.value?.toLowerCase().endsWith(".html") ||
      p.value?.toLowerCase().endsWith(".css") ||
      p.value?.toLowerCase().endsWith(".js")
  );

  if (hasArchiveProp) {
    comp.properties.push({
      name: "bsi:component:archive",
      value: hasArchiveProp.name
    });
  }

  if (hasExecutableProp) {
    comp.properties.push({
      name: "bsi:component:executable",
      value: hasExecutableProp.name
    })
  }

    if (hasStructureProp) {
    comp.properties.push({
      name: "bsi:component:structured",
      value: hasStructureProp.name
    })
  }
}

fs.writeFileSync("sbom-custom.json", JSON.stringify(sbom, null, 2));
console.log("✅ Custom SBOM written to sbom-custom.json");
