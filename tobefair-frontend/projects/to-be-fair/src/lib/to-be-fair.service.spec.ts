import { TestBed } from '@angular/core/testing';

import { ToBeFairService } from './to-be-fair.service';

describe('ToBeFairService', () => {
  let service: ToBeFairService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ToBeFairService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
