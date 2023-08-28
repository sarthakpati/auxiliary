import nibabel as nib


def write_nifti(input_array, reference_nifti_path, output_nifti_path):
    reference = nib.load(reference_nifti_path)

    the_nifti = nib.Nifti1Image(input_array, reference.affine, reference.header)
    nib.save(the_nifti, output_nifti_path)


def read_nifti(input_nifti_path):
    the_nifti = nib.load(input_nifti_path)
    return the_nifti.get_fdata()
