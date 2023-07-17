with (import <nixpkgs> {}).pkgs;

let
    kociemba = python310.pkgs.buildPythonPackage rec {
      pname = "kociemba";
      version = "1.2.1";

      src = python310.pkgs.fetchPypi {
        inherit pname version;
        sha256 = "b77435d7b0e93e9c7963e487e8cc3820540bd1c9bb9fe5665999d3a8deac9ee6";
      };

      doCheck = false;
      #propagatedBuildInputs = [ python310.pkgs.pbr ];
      buildInputs = [ python310Packages.cffi python310Packages.pytest python310Packages.pytest-runner python310Packages.future ];
    };
in mkShell {
  buildInputs = [
    manim
    python310
    kociemba
    ffmpeg
  ];
}