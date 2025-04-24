from pathlib import Path
from typing import Optional

import SimpleITK as sitk
from numpy.typing import NDArray


def write_nifti(
    input_array: NDArray,
    output_nifti_path: str,
    reference_nifti_path: Optional[str] = None,
    create_parent_directory: bool = False,
) -> None:
    """
    Write a NIfTI file from a NumPy array using SimpleITK.

    Args:
        input_array (np.ndarray): The NumPy array containing the data to be written.
        output_nifti_path (str): The path where the output NIfTI file will be saved.
        reference_nifti_path (str, optional): Path to a reference NIfTI file for spatial metadata.
        create_parent_directory (bool): If True, create parent directories if they don't exist.

    Returns:
        None
    """
    # Convert NumPy array to SimpleITK image (zyx expected)
    image = sitk.GetImageFromArray(input_array)

    if reference_nifti_path:
        reference = sitk.ReadImage(reference_nifti_path)
        image.CopyInformation(reference)

    if create_parent_directory:
        parent_dir = Path(output_nifti_path).parent
        parent_dir.mkdir(parents=True, exist_ok=True)

    sitk.WriteImage(image, output_nifti_path)


def read_nifti(
    input_nifti_path: str,
    maintain_dtype: bool = True,
) -> NDArray:
    """
    Read a NIfTI file and return its data as a NumPy array.

    Args:
        input_nifti_path (str): Path to the input NIfTI file.
        maintain_dtype (bool, optional): If True, maintain the data type of the NIfTI data.
                                         If False, allow data type conversion to float. Default is True.

    Returns:
        numpy.ndarray: NIfTI data as a NumPy array.
    """

    image = sitk.ReadImage(input_nifti_path)
    if maintain_dtype:
        array = sitk.GetArrayFromImage(image)
    else:
        array = sitk.GetArrayFromImage(sitk.Cast(image, sitk.sitkFloat32))

    return array
