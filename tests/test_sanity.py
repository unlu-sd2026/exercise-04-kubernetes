from pathlib import Path

def test_k8s_dir_has_manifests():
    ymls = list(Path("k8s").glob("*.yml"))
    assert len(ymls) >= 3, f"k8s/ needs at least 3 manifests, found {len(ymls)}"