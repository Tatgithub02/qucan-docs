# Upload blocks

Four block types under [Upload](tools.md#upload) bring outside files onto the canvas: **Image**, **PDF**, **Python**, and **OpenQASM**. Each starts as an empty drop zone you drop a file onto (or, for Python and OpenQASM, write directly), and can be expanded to a fullscreen view.

## Image

An empty **Image** block prompts you to drop or choose a file:

![Empty Image block, prompting to drop or choose an image](../images/upload/image-empty.png)

Once uploaded, the image renders directly in the block:

![Image block showing an uploaded image](../images/upload/image-preview.png){ .doc-image--portrait }

Click the expand icon (top right of the block) to view the image fullscreen:

![Image expanded to a fullscreen view](../images/upload/image-expanded.png)

<div class="doc-image-end"></div>

## PDF

A **PDF** block shows the document in a paginated viewer, with arrows on either side to move between pages:

![PDF block showing a document, with page navigation arrows](../images/upload/pdf-preview.png)

Click the expand icon (top left of the block) to view the PDF fullscreen, with the same page navigation:

![PDF expanded to a fullscreen view](../images/upload/pdf-expanded.png)

## Python

An empty **Python** block lets you either upload an existing `.py` file, or click **Create a new Python file** to start writing one directly on the canvas:

![Empty Python block, with options to drop a .py file or create a new one](../images/upload/python-empty.png)

Once it has code, the block's header shows a filename, a **Run** button, and a **Download** icon, with an **Output** panel underneath:

![Python block with code, showing Run and Download in the header, and an empty Output panel](../images/upload/python-code.png)

Clicking **Run** shows a spinner while the code executes:

![Python block running, with a spinner replacing the Run button](../images/upload/python-running.png)

Once it finishes, **Output** fills in with whatever the script printed:

![Python block after running, with Output showing the script's printed results](../images/upload/python-output.png)

### Renaming

Click the filename to rename it, the same editable-field pattern used to rename the [workspace itself](customizing.md#name):

![Renaming a Python block's filename](../images/upload/python-rename.png)

A Python block after being renamed:

![Python block renamed to lala.py](../images/upload/python-renamed.png)

### Downloading

Click the download icon in the header to download the block's code as a `.py` file.

## OpenQASM

An empty **OpenQASM file** block lets you either upload an existing `.qasm` file, or create a new one, choosing between **OpenQASM 2.0** and **3.0**:

![Empty OpenQASM file block, with options to drop a .qasm file or create a new 2.0 or 3.0 file](../images/upload/openqasm-empty.png)

Creating a new file starts you off with a minimal Bell-state program, ready to edit, in the version you picked:

=== "OpenQASM 2.0"

    ![New OpenQASM 2.0 file with a Bell-state program](../images/upload/openqasm-2-0.png)

=== "OpenQASM 3.0"

    ![New OpenQASM 3.0 file with a Bell-state program](../images/upload/openqasm-3-0.png)

### Converting to a circuit

Click **Convert to circuit** (top of the block) to turn the code into an editable [Circuit](circuit-block.md) block on the same canvas:

![Circuit block created by converting the OpenQASM file, showing the same H + CNOT + measurement program](../images/upload/openqasm-2-0-converted.png)
