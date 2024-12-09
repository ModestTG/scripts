{
  description = "Immich Date Switcher";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11";
  };
  outputs =
    { self, nixpkgs }:
    let
      pkgs = import nixpkgs {
        system = "x86_64-linux";
      };
    in
    {
      packages.x86_64-linux.go-exiftool = pkgs.buildGoModule rec {
        pname = "go-exiftool";
        version = "v1.10.0";

        src = pkgs.fetchFromGitHub {
          owner = "barasher";
          repo = "go-exiftool";
          rev = "${version}";
          sha256 = "sha256-MfJy2fkq2RXcLJtKeAg4sS1HJveZLttvPYr26UxD9VI=";
        };
        vendorHash = "sha256-PevbolKYoc0Z0cQ5F7fn0Ow4kNJtMTTNFIDO3ZOCLwI=";
        doCheck = false; # skip checkPhase
      };
      devShells.x86_64-linux.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          exiftool
          go
          gopls
          gotools
          go-tools
          self.packages.x86_64-linux.go-exiftool
        ];
      };
    };
}
