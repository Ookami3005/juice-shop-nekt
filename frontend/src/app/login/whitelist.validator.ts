import { AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';

export function whitelistValidator(pattern: string): ValidatorFn {
  const regex = new RegExp(`^[${pattern}]*$`, 'u');

  return (control: AbstractControl): ValidationErrors | null => {
    const raw = control.value;
    if (raw == null || raw === '') return null;

    const value = String(raw);
    return regex.test(value) ? null : { whitelist: true };
  };
}
