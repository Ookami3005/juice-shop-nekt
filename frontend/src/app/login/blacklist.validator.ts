import { AbstractControl, ValidationErrors, ValidatorFn } from '@angular/forms';

function escapeRegexChars(chars: string[]): string[] {
  return chars.map(c => c.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
}

export function blacklistValidator(forbiddenChars: string[]): ValidatorFn {
  const escapedChars = escapeRegexChars(forbiddenChars);
  const regex = new RegExp(`[${escapedChars.join('')}]`);

  return (control: AbstractControl): ValidationErrors | null => {
    if (!control.value) return null;

    const sanitizedValue = control.value.replace(/\s/g, '');

    return regex.test(sanitizedValue) ? { forbiddenChars: true } : null;
  };
}
