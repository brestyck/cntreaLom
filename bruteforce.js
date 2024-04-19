function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function atoa(dec, base) {
  return (dec >>> 0).toString(base);
}

// Set (min, max, timeout) as a interval
async function bruteforce(a, b, t, s, base) {
	// var field = document.getElementById(form_id)
	for (var i = a; i < b; i = i + s) {
		var field = document.getElementsByClassName("form form_input")[0]
		console.log("["+i+"] ANSWER INSERTED");
		if (base != 10) {
			field.value = atoa(i, base);
		} else {
			field.value = i;
		}
		// field.value = i.toString(16);
		// click button in cntrea
		submitForms()
		await sleep(t);
	}
}

var a = 0;
var b = 0;
var d = 0;
var bm = false;

function runbrute() {
	bm = Boolean(document.getElementById("bmEnabledId").checked);
	a = Number(document.getElementById("asel").value)
	b = Number(document.getElementById("bsel").value)
	d = Number(document.getElementById("dsel").value)
	s = Number(document.getElementById("stepsel").value)
	atoabase = Number(document.getElementById("atoabase").value)
	const node = document.getElementById("cntreabrutenode")
	node.hidden = true;
	if (bm == true) {
		console.log("[ATOA] Running with custom base");
		bruteforce(a, b, d, s, atoabase);
	} else {
		console.log("[ATOA] Running with base 10");
		bruteforce(a, b, d, s, 10);
	}
}

function toggle_brutebox() {
	// Create box
	const node = document.createElement("div");
	node.id = "cntreabrutenode"
	node.classList.add("bruteforce_box")
	
	const textnode = document.createTextNode(" Cntrea bruteforce client ");
	const aselector = document.createElement("input");
	aselector.placeholder = "Enter left border";
	aselector.id = "asel";
	
	const bselector = document.createElement("input");
	bselector.id = "bsel";
	bselector.placeholder = "Enter right border";
	
	const dselector = document.createElement("input");
	dselector.id = "dsel";
	dselector.placeholder = "Enter delay (ms)";
	
	const sselector = document.createElement("input");
	sselector.id = "stepsel";
	sselector.placeholder = "Enter step (1 by default)";
	sselector.value = 1;
	
	const binModeEnabled = document.createElement("input");
	binModeEnabled.type = "checkbox";
	binModeEnabled.id = "bmEnabledId";
	
	const baseselector = document.createElement("input");
	baseselector.id = "atoabase";
	baseselector.placeholder = "Enter base (blank for 10)";
	
	const confirmation = document.createElement("button");
	confirmation.id = "cbtn"
	confirmation.addEventListener("click", runbrute)
	confirmation.classList.add("form_submit")
	confirmation.appendChild(document.createTextNode("RUN"))
	
	node.appendChild(textnode);
	node.appendChild(document.createElement("br"))
	node.appendChild(aselector)
	node.appendChild(document.createElement("br"))
	node.appendChild(bselector)
	node.appendChild(document.createElement("br"))
	node.appendChild(sselector)
	node.appendChild(document.createElement("br"))
	node.appendChild(dselector)
	node.appendChild(document.createElement("br"))
	node.appendChild(confirmation)
	node.appendChild(document.createElement("br"))
	node.appendChild(document.createElement("br"))
	node.appendChild(binModeEnabled)
	node.appendChild(document.createTextNode("Generate in atoa"))
	node.appendChild(document.createElement("br"))
	node.appendChild(baseselector)
	document.getElementById("dom_root").appendChild(node);
}

toggle_brutebox()
